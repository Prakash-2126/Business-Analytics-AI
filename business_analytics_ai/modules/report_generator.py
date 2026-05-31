from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class ReportGenerator:

    @staticmethod
    def generate(
        profile,
        descriptive,
        recommendations
    ):

        doc = SimpleDocTemplate(
            "reports/business_report.pdf"
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "Business Analytics Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        content.append(
            Paragraph(
                "Data Profile",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(profile),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        content.append(
            Paragraph(
                "Descriptive Analysis",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(descriptive),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        content.append(
            Paragraph(
                "Recommendations",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(recommendations),
                styles["BodyText"]
            )
        )

        doc.build(content)