get_job = {
    "job" : "한전",
    "type" : "공기업"
}
print(get_job)
get_job["salary"] = "4000만원"
get_job["job"] = "삼성SDS"
print(get_job)

del get_job["type"]
print(get_job)