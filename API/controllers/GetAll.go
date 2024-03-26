package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)

type DbStructure struct {
	SiteName string
	RouteType string
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
    Routes []NestedRoute
}

// Determine if NestedSite already exists for the current site. If it does, append the current route tot he existing NestedSite, 
// if it doesn't, create a new NestedSite for the current site. 
func findSiteIndex(nestedRoutes []NestedSite, siteName string) int {
    for i, nestedRoute := range nestedRoutes {
        if nestedRoute.SiteName == siteName {
            return i // Return the index of the site if found
        }
    }
    return -1 // Return -1 if the site is not found
}


func GetAll(c *gin.Context) {
	// Get all sites names, routes and routes counts data
	var allNestedRoutes []NestedSite 

		var siteRouteContent []DbStructure
	result := initializers.DB.Table("site_route_content" ).Select("site_name", "route_type", "route_count").Find(&siteRouteContent)

	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	for _, route := range siteRouteContent {
		nestedRoute := NestedRoute{
			RouteType: route.RouteType,
			RouteCount: route.RouteCount,
		}
		siteIndex := findSiteIndex(allNestedRoutes, route.SiteName)
		if siteIndex == -1 {
			allNestedRoutes = append(allNestedRoutes, NestedSite{
				SiteName: route.SiteName,
				Routes: []NestedRoute{nestedRoute},
			})
		} else {
			allNestedRoutes[siteIndex].Routes = append(allNestedRoutes[siteIndex].Routes, nestedRoute)
		}
	}

	// Return the list of sites names, routes and routes counts data in the JSON response
	c.JSON(http.StatusOK, gin.H{
		"message": "All routes and their counts of all sites",
		"data": allNestedRoutes,
	})
}

