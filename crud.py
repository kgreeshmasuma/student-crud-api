from sqlalchemy.orm import Session

from models import Student
from schemas import StudentCreate, StudentUpdate


def create_student(db: Session, student: StudentCreate):
    student_data = student.model_dump()
    db_student = Student(**student_data)

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def update_student(
    db: Session,
    db_student: Student,
    student_update: StudentUpdate
):
    update_data = student_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(db: Session, db_student: Student):
    db.delete(db_student)
    db.commit()