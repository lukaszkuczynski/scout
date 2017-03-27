from unittest import main, TestCase
from application.reporter import ReporterFactory

class MailReporterTest(TestCase):

    def test_reporter_sends_mail(self):
        mission = {
            "mission": {
                "reporter": {
                    "mail": {
                        "to": ["kuczynskilukasz@gmail.com"]
                    }
                }
            }
        }
        reporter = ReporterFactory(mission).reporter()
        reporter.report("This is sent during integration test of Scout's mail reporter")

if __name__ == '__main__':
    main()