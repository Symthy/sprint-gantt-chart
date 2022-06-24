# Sprint Gantt Chart Template Builder

1 Sprint (2 weeks) 分の ガントチャート(plantuml) 雛形ファイルを生成

required: docker

## tool run

```
cp conf/members.yml.model conf/members.yml
```

members.yml に チームメンバーの名前を箇条書き

```
./run.sh <Sprint Number>
```

members.yml に記載人数分のタスクを入力

- Task ID と Task Title を聞かれるため入力
- Task ID 未入力で Enter を押すと、次の人の入力に進む

out フォルダに .pu ファイル出力
