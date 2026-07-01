import pandas as pd
data = {
    "Team": ["CSK","MI","RCB","CSK","MI","RCB","CSK","MI"],
    "Player": ["Dhoni","Rohit","Virat","Jadeja","Surya","Maxwell","Gaikwad","Bumrah"],
    "Runs": [40,55,70,35,65,20,80,10],
    "Wickets": [0,0,0,2,0,1,0,3]
}

df = pd.DataFrame(data)
print(df)
s=df.groupby("Team")["Runs"].sum()
print(s)
print(df.loc[df["Runs"].idxmax()])
print(df.groupby("Team")["Wickets"].max())
print(df.groupby("Player")["Runs"].mean())
print(df.loc[(df["Runs"]>50 )|(df["Wickets"]>=2)])
print(df)
print("no. of players in CSK: ",(df["Team"]=="CSK").sum())
print(df.groupby("Team").value_counts().tolist())