from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "crm.sqlite"
SEED_PATH = ROOT / "data" / "crm.json"


def connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with connect() as connection:
        create_schema(connection)
        if is_empty(connection):
            seed_from_json(connection)


def get_crm_data() -> dict[str, list[dict[str, Any]]]:
    with connect() as connection:
        return {
            "accounts": fetch_all(connection, "accounts"),
            "opportunities": fetch_all(connection, "opportunities"),
            "contacts": fetch_all(connection, "contacts"),
            "tasks": fetch_all(connection, "tasks"),
            "activities": fetch_all(connection, "activities"),
        }


def create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        create table if not exists accounts (
          id text primary key,
          name text not null,
          industry text not null,
          segment text not null,
          owner text not null,
          health text not null,
          arr integer not null,
          renewalDate text not null
        );

        create table if not exists opportunities (
          id text primary key,
          accountId text not null references accounts(id),
          name text not null,
          stage text not null,
          amount integer not null,
          probability integer not null,
          closeDate text not null,
          nextStep text not null,
          lastActivityDays integer not null,
          contactCoverage integer not null
        );

        create table if not exists contacts (
          id text primary key,
          accountId text not null references accounts(id),
          name text not null,
          role text,
          influence text,
          lastContactedDays integer
        );

        create table if not exists tasks (
          id text primary key,
          accountId text not null references accounts(id),
          title text not null,
          dueDate text not null,
          status text not null,
          priority text not null
        );

        create table if not exists activities (
          id text primary key,
          accountId text not null references accounts(id),
          type text not null,
          date text not null,
          summary text not null
        );
        """
    )


def is_empty(connection: sqlite3.Connection) -> bool:
    row = connection.execute("select count(*) as count from accounts").fetchone()
    return row["count"] == 0


def seed_from_json(connection: sqlite3.Connection) -> None:
    data = json.loads(SEED_PATH.read_text())

    insert_many(connection, "accounts", data["accounts"])
    insert_many(connection, "opportunities", data["opportunities"])
    insert_many(connection, "contacts", data["contacts"])
    insert_many(connection, "tasks", data["tasks"])
    insert_many(connection, "activities", data["activities"])


def insert_many(connection: sqlite3.Connection, table: str, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return

    columns = list(rows[0])
    placeholders = ", ".join("?" for _ in columns)
    column_list = ", ".join(columns)
    values = [[row.get(column) for column in columns] for row in rows]

    connection.executemany(
        f"insert into {table} ({column_list}) values ({placeholders})",
        values,
    )


def fetch_all(connection: sqlite3.Connection, table: str) -> list[dict[str, Any]]:
    rows = connection.execute(f"select * from {table} order by id").fetchall()
    return [dict(row) for row in rows]
