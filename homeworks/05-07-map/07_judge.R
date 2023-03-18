library(data.table)
library(ggplot2)
this.dir <- "~/teaching/cs470-570-spring-2023/homeworks/05-07-map/"
setwd(this.dir)
py.file.vec <- Sys.glob("07_judge/*.py")
get.out <- function(file.py, suffix="path", txt.file="50test.txt", search.type="DEPTH", start="A", goal="B"){
  out.txt <- sub(".txt$", paste0("_", suffix, ".txt"), txt.file)
  unlink(out.txt)
  cmd <- paste(
    paste0("PYTHONPATH=", this.dir),
    "python3", file.py, txt.file, search.type, start, goal)
  system(cmd)
  tryCatch({
    readLines(out.txt)[1]
  }, error=function(e){
    NA_character_
  })
}
solution <- get.out("solution.py", "solution")

result.dt.list <- list()
system("python3 --version")
for(py.file in py.file.vec){
  for(iteration in 1:3){
    timing <- system.time({
      path <- get.out(py.file, "path")
    })
    result.dt.list[[paste(py.file, iteration)]] <- data.table(
      program=gsub("07_judge/|.py","",py.file), iteration,
      path,
      correct=identical(path, solution),
      seconds=timing[["elapsed"]])
  }
}
result.dt <- rbindlist(result.dt.list)
tibble::tibble(result.dt)

zero.err <- result.dt[correct==TRUE]
zero.err[, median := median(seconds), by=program]
setkey(zero.err, median)
zero.err[, Program := factor(program, unique(program))]
ggplot()+
  geom_point(aes(
    seconds, Program),
    data=zero.err)
    
