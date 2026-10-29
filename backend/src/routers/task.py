from fastapi import APIRouter, Depends, HTTPException
from ..schemas import TaskCreate
from ..database import session, get_db
from ..models import Task
from sqlalchemy.orm import Session
from ..security import auth

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/create-task")
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    try:
        new_task = Task(**task.model_dump(), user_id = current_user.id)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except Exception as e:
        print(f" Error {e}")

@router.get("/get-tasks")
def get_tasks(db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    try:
        tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
        return tasks
    except Exception as e:
        print(f" Error {e}")
        
@router.get("/get-task/{id}")
def get_task_by_id(id: int, db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    task_by_id = db.query(Task).filter(Task.id == id).first()
    if not task_by_id:
        raise HTTPException(status_code = 404, detail="Task not found")
    if task_by_id.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not Authorized to access this task")
    return task_by_id

@router.put("/update-task")
def update_task(id: int, task: TaskCreate, db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    task_exist = db.query(Task).filter(Task.id == id).first()
    if task_exist.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not Authorized to access this task")
    if not task_exist:
        raise HTTPException(status_code=404, detail="Task not found")
    task_exist.title = task.title
    task_exist.description = task.description
    task_exist.completed = task.completed
    
    # for key, value in task.model_dump().items():
    #     setattr(task_exist, key, value)
    
    db.commit()
    db.refresh(task_exist)
    return task_exist

@router.delete("/delete-task")
def delete_task(id: int, db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    task_exist = db.query(Task).filter(Task.id == id).first()
    if task_exist.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not Authorized to access this task")
    if not task_exist:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task_exist)
    db.commit()
    return {"message": "Task is deleted"}