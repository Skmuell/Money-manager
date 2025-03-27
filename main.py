from db import get_session

if __name__ == "__main__":
    from sqlalchemy import text

    with get_session() as session:
        print("## Testing database connection...")
        result = session.execute(text("SELECT 1"))

        if result.scalar() == 1:
            print("## Connection test successful!")
        else:
            print("## Connection test failed.")