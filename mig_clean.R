library(tidyverse)
tb <- read_csv("cso_migration.csv",col_names = TRUE, skip = 2)
tb <- tb[1:8,]
a <- gather(tb, key = year_number, value = head_count, -X1)
n <- c('key','year_number','head_count')
colnames(a) <- c('key','year_number','head_count')
b <- mutate(a, head_singles = head_count * 1000)
write.csv(b, "migration.csv")