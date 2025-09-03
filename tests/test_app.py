import pexpect
import os

COBOL_BINARY = os.path.abspath("../modernize-legacy-cobol-app-main/accountsystem")
PROMPT_MESSAGE = r"Enter your choice \(1-4\):"
EXIT_MESSAGE = "Exiting the program. Goodbye!"


class TestDataProgram:
    """
    Tests for data-related operations such as viewing the initial balance.
    """

    def test_read_initial_balance(self):
        child = pexpect.spawn(COBOL_BINARY, encoding='utf-8')
        child.expect(PROMPT_MESSAGE, timeout=5)
        child.sendline("1")
        child.expect(PROMPT_MESSAGE, timeout=5)
        assert "Current balance: 001000.00" in child.before
        child.sendline("4")
        child.expect(EXIT_MESSAGE, timeout=5)

class TestOperationsProgram:
    """
    Tests for account operations (credit and debit).
    """

    def test_credit_valid_amount(self):
        child = pexpect.spawn(COBOL_BINARY, encoding='utf-8')
        child.expect(PROMPT_MESSAGE, timeout=5)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=5)
        child.sendline("100")
        child.expect(PROMPT_MESSAGE, timeout=5)
        assert "Amount credited. New balance: 001100.00" in child.before
        child.sendline("4")
        child.expect(EXIT_MESSAGE, timeout=5)

    def test_credit_zero_amount(self):
        child = pexpect.spawn(COBOL_BINARY, encoding='utf-8')
        child.expect(PROMPT_MESSAGE, timeout=5)
        child.sendline("2")
        child.expect("Enter credit amount:", timeout=5)
        child.sendline("0")
        child.expect(PROMPT_MESSAGE, timeout=5)
        assert "Amount credited. New balance: 001000.00" in child.before
        child.sendline("4")
        child.expect(EXIT_MESSAGE, timeout=5)

    def test_debit_valid_amount(self):
        child = pexpect.spawn(COBOL_BINARY, encoding='utf-8')
        child.expect(PROMPT_MESSAGE, timeout=5)
        child.sendline("3")
        child.expect("Enter debit amount:", timeout=5)
        child.sendline("50")
        child.expect(PROMPT_MESSAGE, timeout=5)
        assert "Amount debited. New balance: 000950.00" in child.before
        child.sendline("4")
        child.expect(EXIT_MESSAGE, timeout=5)

    def test_debit_greater_than_balance(self):
        child = pexpect.spawn(COBOL_BINARY, encoding='utf-8')
        child.expect(PROMPT_MESSAGE, timeout=5)
        child.sendline("3")
        child.expect("Enter debit amount:", timeout=5)
        child.sendline("2000.00")
        child.expect(PROMPT_MESSAGE, timeout=5)
        assert "Insufficient funds for this debit." in child.before
        child.sendline("4")
        child.expect(EXIT_MESSAGE, timeout=5)

    def test_debit_zero_amount(self):
        child = pexpect.spawn(COBOL_BINARY, encoding='utf-8')
        child.expect(PROMPT_MESSAGE, timeout=5)
        child.sendline("3")
        child.expect("Enter debit amount:", timeout=5)
        child.sendline("0.00")
        child.expect(PROMPT_MESSAGE, timeout=5)
        assert "Amount debited. New balance: 001000.00" in child.before
        child.sendline("4")
        child.expect(EXIT_MESSAGE, timeout=5)

class TestMainProgram:
    """
    Tests for main program control flow, especially clean exit.
    """

    def test_exit_application(self):
        child = pexpect.spawn(COBOL_BINARY, encoding='utf-8')
        child.expect(PROMPT_MESSAGE, timeout=5)
        child.sendline("4")
        child.expect(EXIT_MESSAGE, timeout=5)
        child.expect(pexpect.EOF, timeout=5)
        assert child.wait() == 0
