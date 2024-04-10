# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .api_meta import ApiMeta
from .chat_citation import ChatCitation
from .chat_document import ChatDocument
from .chat_message import ChatMessage
from .chat_search_query import ChatSearchQuery
from .chat_search_result import ChatSearchResult
from .finish_reason import FinishReason
from .tool_call import ToolCall


class NonStreamedChatResponse(UncheckedBaseModel):
    text: str = pydantic_v1.Field()
    """
    Contents of the reply generated by the model.
    """

    generation_id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Unique identifier for the generated reply. Useful for submitting feedback.
    """

    citations: typing.Optional[typing.List[ChatCitation]] = pydantic_v1.Field(default=None)
    """
    Inline citations for the generated reply.
    """

    documents: typing.Optional[typing.List[ChatDocument]] = pydantic_v1.Field(default=None)
    """
    Documents seen by the model when generating the reply.
    """

    is_search_required: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Denotes that a search for documents is required during the RAG flow.
    """

    search_queries: typing.Optional[typing.List[ChatSearchQuery]] = pydantic_v1.Field(default=None)
    """
    Generated search queries, meant to be used as part of the RAG flow.
    """

    search_results: typing.Optional[typing.List[ChatSearchResult]] = pydantic_v1.Field(default=None)
    """
    Documents retrieved from each of the conducted searches.
    """

    finish_reason: typing.Optional[FinishReason] = None
    tool_calls: typing.Optional[typing.List[ToolCall]] = None
    chat_history: typing.Optional[typing.List[ChatMessage]] = pydantic_v1.Field(default=None)
    """
    A list of previous messages between the user and the model, meant to give the model conversational context for responding to the user's `message`.
    """

    meta: typing.Optional[ApiMeta] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
