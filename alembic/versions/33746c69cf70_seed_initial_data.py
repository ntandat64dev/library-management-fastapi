"""Seed initial data

Revision ID: 33746c69cf70
Revises: f355eb62a289
Create Date: 2025-08-05 21:38:43.287393

"""

from datetime import datetime
from typing import Sequence, Union
from uuid import uuid4

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "33746c69cf70"
down_revision: Union[str, Sequence[str], None] = "f355eb62a289"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


genre_table = sa.table(
    "genre",
    sa.column("id", sa.Uuid),
    sa.column("name", sa.String),
    sa.column("created_by", sa.String),
    sa.column("created_at", sa.DateTime),
    sa.column("updated_by", sa.String),
    sa.column("updated_at", sa.DateTime),
)


book_table = sa.table(
    "book",
    sa.column("id", sa.Uuid),
    sa.column("isbn", sa.String),
    sa.column("title", sa.String),
    sa.column("author", sa.String),
    sa.column("publisher", sa.String),
    sa.column("publish_date", sa.DateTime),
    sa.column("genre_id", sa.Uuid),
    sa.column("language", sa.String),
    sa.column("dimension", sa.String),
    sa.column("total_copies", sa.Integer),
    sa.column("available_copies", sa.Integer),
    sa.column("created_by", sa.String),
    sa.column("created_at", sa.DateTime),
    sa.column("updated_by", sa.String),
    sa.column("updated_at", sa.DateTime),
)


def upgrade() -> None:
    """Upgrade schema."""

    # Insert initial data into the genre table

    op.bulk_insert(
        genre_table,
        [
            {
                "id": "1e69b10e-fb2f-4805-bb72-66d612353bef",
                "name": "Fiction",
                "created_by": "system",
                "created_at": str(datetime.now()),
            },
            {
                "id": "2e69b10e-fb2f-4805-bb72-66d612353bef",
                "name": "Non-Fiction",
                "created_by": "system",
                "created_at": str(datetime.now()),
            },
            {
                "id": "3e69b10e-fb2f-4805-bb72-66d612353bef",
                "name": "Science Fiction",
                "created_by": "system",
                "created_at": str(datetime.now()),
            },
            {
                "id": "4e69b10e-fb2f-4805-bb72-66d612353bef",
                "name": "Fantasy",
                "created_by": "system",
                "created_at": str(datetime.now()),
            },
            {
                "id": "5e69b10e-fb2f-4805-bb72-66d612353bef",
                "name": "Mystery",
                "created_by": "system",
                "created_at": str(datetime.now()),
            },
        ],
    )

    # Insert initial data into the book table
    op.bulk_insert(
        book_table,
        [
            {
                "id": uuid4(),
                "isbn": "9781234567897",
                "title": "Introduction to Python Programming",
                "author": "John Doe",
                "publisher": "Tech Press",
                "publish_date": "2008-08-11T12:00:00",
                "genre_id": "1e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "8.5x11",
                "total_copies": 10,
                "available_copies": 10,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9780135166307",
                "title": "Introduction to Python Programming",
                "author": "John Doe",
                "publisher": "Tech Press",
                "publish_date": "2008-08-11T12:00:00",
                "genre_id": "1e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "8.5x11",
                "total_copies": 10,
                "available_copies": 10,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9781492056355",
                "title": "Advanced Python Techniques",
                "author": "Jane Smith",
                "publisher": "Code Masters",
                "publish_date": "2012-05-22T09:30:00",
                "genre_id": "2e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "7x10",
                "total_copies": 15,
                "available_copies": 12,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9780596158101",
                "title": "Data Science with Python",
                "author": "Alice Johnson",
                "publisher": "Data World",
                "publish_date": "2015-11-10T14:45:00",
                "genre_id": "3e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "6x9",
                "total_copies": 20,
                "available_copies": 18,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9781491978917",
                "title": "Flask Web Development",
                "author": "Robert Brown",
                "publisher": "Webify Books",
                "publish_date": "2016-07-18T08:20:00",
                "genre_id": "4e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "8x10",
                "total_copies": 8,
                "available_copies": 5,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9781787285213",
                "title": "Machine Learning in Action",
                "author": "Catherine Lee",
                "publisher": "AI Press",
                "publish_date": "2018-03-05T11:15:00",
                "genre_id": "5e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "7.5x9.5",
                "total_copies": 12,
                "available_copies": 12,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9780134845623",
                "title": "Python for Data Analysis",
                "author": "Michael Davis",
                "publisher": "Data Insights",
                "publish_date": "2017-10-01T16:00:00",
                "genre_id": "2e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "8x10",
                "total_copies": 25,
                "available_copies": 22,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9781492041139",
                "title": "Effective Python",
                "author": "Laura White",
                "publisher": "Pragmatic Coders",
                "publish_date": "2019-06-25T13:30:00",
                "genre_id": "3e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "6x9",
                "total_copies": 18,
                "available_copies": 14,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9780134692883",
                "title": "Python Cookbook",
                "author": "Steven Clarke",
                "publisher": "Recipes Publishing",
                "publish_date": "2020-01-15T10:10:00",
                "genre_id": "2e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "7x9",
                "total_copies": 30,
                "available_copies": 30,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
            {
                "id": uuid4(),
                "isbn": "9781492071266",
                "title": "Django by Example",
                "author": "Patricia Green",
                "publisher": "Webify Books",
                "publish_date": "2021-02-28T15:50:00",
                "genre_id": "1e69b10e-fb2f-4805-bb72-66d612353bef",
                "language": "en",
                "dimension": "8.5x11",
                "total_copies": 9,
                "available_copies": 7,
                "created_by": "system",
                "created_at": str(datetime.now()),
                "updated_by": None,
                "updated_at": None,
            },
        ],
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""

    # Delete data from the book table
    op.execute(
        sa.delete(book_table).where(
            book_table.c.isbn.in_(
                [
                    "9781234567897",
                    "9780135166307",
                    "9781492056355",
                    "9780596158101",
                    "9781491978917",
                    "9781787285213",
                    "9780134845623",
                    "9781492041139",
                    "9780134692883",
                    "9781492071266",
                ]
            )
        )
    )

    # Delete data from the genre table
    op.execute(
        sa.delete(genre_table).where(
            genre_table.c.id.in_(
                [
                    "1e69b10e-fb2f-4805-bb72-66d612353bef",
                    "2e69b10e-fb2f-4805-bb72-66d612353bef",
                    "3e69b10e-fb2f-4805-bb72-66d612353bef",
                    "4e69b10e-fb2f-4805-bb72-66d612353bef",
                    "5e69b10e-fb2f-4805-bb72-66d612353bef",
                ]
            )
        )
    )

    pass
