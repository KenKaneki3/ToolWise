import argparse
from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()


def display_results(query: str, result) -> None:
    print(f"\n📊 Results for: {query}")
    print("=" * 60)

    for i, company in enumerate(result.companies, 1):
        print(f"\n{i}. 🏢 {company.name}")
        print(f"   🌐 Website: {company.website}")
        print(f"   💰 Pricing: {company.pricing_model}")
        print(f"   📖 Open Source: {company.is_open_source}")

        if company.tech_stack:
            print(f"   🛠️  Tech Stack: {', '.join(company.tech_stack[:5])}")

        if company.language_support:
            print(f"   💻 Language Support: {', '.join(company.language_support[:5])}")

        if company.api_available is not None:
            api_status = "✅ Available" if company.api_available else "❌ Not Available"
            print(f"   🔌 API: {api_status}")

        if company.integration_capabilities:
            print(f"   🔗 Integrations: {', '.join(company.integration_capabilities[:4])}")

        if company.description and company.description != "Analysis failed":
            print(f"   📝 Description: {company.description}")

        print()

    if result.analysis:
        print("Developer Recommendations: ")
        print("-" * 40)
        print(result.analysis)


def main():
    parser = argparse.ArgumentParser(description="Developer Tools Research Agent")
    parser.add_argument("query", type=str, nargs="?", default=None, help="The developer tools query to research.")
    args = parser.parse_args()

    workflow = Workflow()
    print("Developer Tools Research Agent")

    if args.query:
        print(f"\n🔍 Developer Tools Query: {args.query}")
        result = workflow.run(args.query)
        display_results(args.query, result)
    else:
        while True:
            query = input("\n🔍 Developer Tools Query: ").strip()
            if query.lower() in {"quit", "exit"}:
                break
            if query:
                result = workflow.run(query)
                display_results(query, result)


if __name__ == "__main__":
    main()
