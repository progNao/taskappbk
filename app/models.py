from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from database import Base

class Comment(Base):
  __tablename__ = "comment"

  id = Column(Integer, primary_key=True, index=True, nullable=False)
  comment = Column(String, index=True)
  ticket_id = Column(String, ForeignKey("ticket.id"))

  ticket = relationship("Ticket", back_populates="comment")



class Ticket(Base):
  __tablename__ = "ticket"

  id = Column(Integer, primary_key=True, index=True, nullable=False)
  title = Column(String, index=True, nullable=False)
  detail = Column(String, index=True)
  deadline = Column(String, index=True, nullable=False)
  priority = Column(String, index=True, nullable=False)
  status = Column(String, index=True, nullable=False)
  manager = Column(String, index=True)

  comment = relationship("Comment", back_populates="ticket")