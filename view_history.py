from history import list_invoices, total_sales


def main():
    records = list_invoices()
    if not records:
        print("No invoices yet.")
        return

    print(f"{'Invoice':<12}{'Date':<12}{'Customer':<22}{'Total (INR)':>14}")
    print("-" * 60)
    for r in records:
        print(f"{r['invoice_number']:<12}{r['date']:<12}"
              f"{r['buyer_name'][:20]:<22}{r['grand_total']:>14}")
    print("-" * 60)
    print(f"{len(records)} invoice(s), total sales: INR {total_sales()}")


if __name__ == "__main__":
    main()