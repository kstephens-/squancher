import logging
import datetime
import uuid
from ..extensions import pgdb
from sqlalchemy.dialects.postgresql import UUID

logger = logging.getLogger(__name__)


class Document(pgdb.Model):
    """ A squanched document """

    document_id = pgdb.Column(UUID(as_uuid=True), primary_key=True,
                              nullable=False, default=lambda: uuid.uuid4(),
                              unique=True)
    user_id = pgdb.Column(UUID(as_uuid=True), nullable=False)
    document = pgdb.Column(pgdb.Text, nullable=False)
    created_datetime = pgdb.Column(pgdb.DateTime(), nullable=False,
                                   default=datetime.datetime.utcnow())
    modified_datetime = pgdb.Column(pgdb.DateTime(), nullable=False,
                                    default=datetime.datetime.utcnow())
