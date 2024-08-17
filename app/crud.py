from sqlalchemy.orm import Session

import models, schemas

def get_tickets(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Ticket).offset(skip).limit(limit).all()

def add_ticket(db: Session, ticket: schemas.TicketRequest):
  new_ticket = models.Ticket(**ticket.dict())
  db.add(new_ticket)
  db.commit()
  db.refresh(new_ticket)
  return new_ticket

def update_ticket(db: Session, ticket: schemas.TicketRequest, id: int):
  db_ticket = db.query(models.Ticket).filter(models.Ticket.id == id).first()
  for field, value in ticket.dict(exclude_unset=True).items():
    setattr(db_ticket, field, value)
  db.commit()
  db.refresh(db_ticket)
  return db_ticket

def get_comment(db: Session, id: int):
  return db.query(models.Comment).filter(models.Comment.ticket_id == id).all()

def add_comment(db: Session, comment: schemas.CommentRequest):
  new_comment = models.Comment(**comment.dict())
  db.add(new_comment)
  db.commit()
  db.refresh(new_comment)
  return new_comment