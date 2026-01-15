"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    status_messages = {
        "success": "Authentication successful",
        "expired": "Password expired",
        "failed": "Authentication failed"
    }

    log_message = (
        f"Login attempt | "
        f"Username = {username} | "
        f"Status = {status} | "
        f"Message = {status_messages.get(status, 'Unknown status')}"
    )

    logging.basicConfig(
        filename="login_system.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        force=True
    )

    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


def test_logger_success():
    log_event(username="admin", status="success")
    with open("login_system.log", "r") as f:
        content = f.read()
        assert "Username: admin, Status: success" in content

def test_logger_expired():
    log_event(username="admin1", status="expired")
    with open("login_system.log", "r") as f:
        content = f.read()
        assert "Username: admin1, Status: expired" in content

def test_logger_failed():
    log_event(username="admin2", status="failed")
    with open("login_system.log", "r") as f:
        content = f.read()
        assert "Username: admin2, Status: failed" in content







