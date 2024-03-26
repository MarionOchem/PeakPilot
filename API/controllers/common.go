package controllers

type DbStructure struct {
	SiteName   string
	RouteType  string
	RouteCount int
}

// Restructuring data before returning it as JSON :
// Gorm maps the columns from the query result to the fields of those structs

// Struct to represent the nested route data
type NestedRoute struct {
	RouteType  string
	RouteCount int
}

// Struct to represent the nested site data
type NestedSite struct {
	SiteName string
	Routes   []NestedRoute
}

type Route struct {
	Name string
}

type Site struct {
	Name string
}

type Response struct {
	Site   string
	Routes []NestedRoute
}