@udf.scalar.python
def check_vuln(name: str, version: str) -> str:
    r = requests.get(f"https://pypi.org/pypi/{name}/{version}/json")
    if bool(vulns := json.loads(r.content.decode())["vulnerabilities"]):
        return [
            {key: val for key, val in entry.items() if key in ("aliases", "fixed_in")}
            for entry in vulns
        ]

pp.mutate(has_vuln=check_vuln(pp.name, pp.version))