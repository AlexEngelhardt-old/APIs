# This is a simple API in R, just to compare.
# Read https://www.rplumber.io/docs/quickstart.html for the source

library(plumber)

#' Echo the parameter that was sent in
#' @param msg The message to echo back.
#' @get /echo
function(msg=""){
  list(msg = paste0("The message is: '", msg, "'"))
}

#' Plot out data from the iris dataset
#' @param spec If provided, filter the data to only this species (e.g. 'setosa')
#' @get /plot
#' @png
function(spec){
  myData <- iris
  title <- "All Species"

  # Filter if the species was specified
  if (!missing(spec)){
    title <- paste0("Only the '", spec, "' Species")
    myData <- subset(iris, Species == spec)
  }

  plot(myData$Sepal.Length, myData$Petal.Length,
       main=title, xlab="Sepal Length", ylab="Petal Length")
}

#' Add two numbers and return the result
#' @param a The first number to add
#' @param b The second number to add
#' @post /sum
addTwo <- function(a, b){
  as.numeric(a) + as.numeric(b)
}

# From an R window, execute:
#
# library(plumber)
# pr <- plumb('01_simple-R-API.R')
# pr$run(port=3090)
#
#
# Then from a new R window, run:
# 
# library(httr)
# > response(POST('http://127.0.0.1:3090/sum', body="a=4&b=17"))
#
#
# Or point your browser e.g. to
#
#  http://127.0.0.1:3090/echo?msg=what's up
#
#
# Or, from the console, e.g.:
#
#  curl --data '{"a":4, "b":13}' http://127.0.0.1:3090/sum

# Also check out
#
# http://127.0.0.1:3090/__swagger__/
#
# for an automatic documentation of your API (built from the
# Roxygen-style comments)
#

