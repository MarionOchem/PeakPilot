// Restructuring db data before returning it as JSON :

package controllers

type DbStructure struct {
	SiteName   string
	RouteType  string
	RouteCount int
}

type Route struct {
	Name string
}

type Site struct {
	Name string
}
type NestedRoute struct {
	RouteType  string
	RouteCount int
}

type NestedSite struct {
	SiteName string
	Routes   []NestedRoute
}

type Response struct {
	Site   string
	Routes []NestedRoute
}