from pydantic import BaseModel
from typing import List

class TicketBase(BaseModel):
  title: str
  detail: str
  deadline: str
  priority: str
  status: str
  manager: str

class TicketRequest(TicketBase):
  class Config:
    orm_mode = True

class Ticket(TicketBase):
  id: int

  class Config:
    orm_mode = True

class TicketResponse(BaseModel):
  data: List[Ticket]


class CommentBase(BaseModel):
  comment: str
  ticket_id: int

class CommentRequest(CommentBase):
  class Config:
    orm_mode = True

class Comment(CommentBase):
  id: int

  class Config:
    orm_mode = True

class CommentResponse(BaseModel):
  data: List[Comment]