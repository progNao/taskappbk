from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 許可するオリジンのリスト
origins = [
    "http://localhost",  # ローカル開発環境
    "http://localhost:3000",  # Vue.jsのデフォルトのポート
    "https://your-domain.com",  # デプロイ後のVue.jsフロントエンドのドメイン
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジンを指定
    allow_credentials=True,  # クレデンシャル（Cookieなど）を許可するか
    allow_methods=["*"],  # 許可するHTTPメソッド（GET, POST, PUTなど）
    allow_headers=["*"],  # 許可するHTTPヘッダー
)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/ticket/", response_model=schemas.TicketResponse)
def get_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  tickets = crud.get_tickets(db, skip=skip, limit=limit)
  return {'data': tickets}

@app.post("/ticket/")
def add_ticket(ticket: schemas.TicketRequest, db: Session = Depends(get_db)):
  crud.add_ticket(db, ticket)
  return {'data': []}

@app.put("/ticket/{ticket_id}")
def update_ticket(ticket_id: int, ticket: schemas.TicketRequest, db: Session = Depends(get_db)):
  crud.update_ticket(db, ticket, ticket_id)
  return {'data': []}

@app.get("/comment/{ticket_id}", response_model=schemas.CommentResponse)
def get_comment_by_ticketId(ticket_id: int, db: Session = Depends(get_db)):
  comments = crud.get_comment(db, ticket_id)
  return {'data': comments}

@app.post("/comment/{ticket_id}")
def add_comment_by_ticketId(comment: schemas.CommentRequest, db: Session = Depends(get_db)):
  crud.add_comment(db, comment)
  return {'data': []}