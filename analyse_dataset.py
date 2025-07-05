import pandas as pd

df = pd.read_excel("shared_templates_feature_usage_cleaned.xlsx")

print("\n=== USER SEGMENTATION ===")
print("Role Distribution:\n", df['role'].value_counts())
print("\nPlan Distribution:\n", df['plan_type'].value_counts())

avg_created = df['total_templates_created'].mean()
avg_shared = df['total_templates_shared'].mean()
avg_used = df['template_used_by_others'].mean()

print(f"\nAverage Templates Created per User: {avg_created:.2f}")
print(f"Average Templates Shared per User: {avg_shared:.2f}")
print(f"Average Times Templates Were Used by Others: {avg_used:.2f}")

# === High and Low Reuse ===
high_reuse = df[df['template_used_by_others'] >= 5]
low_reuse = df[df['template_used_by_others'] == 0]

print(f"\nUsers with High Reuse (≥5 uses):\n{high_reuse[['user_id', 'template_used_by_others']]}")
print(f"\nUsers with No Reuse (0 uses):\n{low_reuse[['user_id', 'template_used_by_others']]}")

# === Reuse Analysis by Plan Type ===
reuse_by_plan = df.groupby('plan_type')['template_used_by_others'].mean()
print("\nAverage Template Reuse by Plan Type:\n", reuse_by_plan)

# === Metric Calculations ===
total_uses = df['template_used_by_others'].sum()
total_shared = df['total_templates_shared'].sum()
value_delivered = total_uses / total_shared if total_shared else 0

print(f"\nTotal Template Uses by Others: {total_uses}")
print(f"Total Templates Shared: {total_shared}")
print(f"Feature Value Delivered (Avg. Uses per Template Shared): {value_delivered:.2f}")
