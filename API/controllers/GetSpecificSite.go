package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)

func GetSpecificSite(c *gin.Context) {
	// Retrieve site parameter from the HTTP request 
	site := c.Param("site")

	var siteRouteContent []DbStructure
	result := initializers.DB.Table("site_route_content").Select("site_name", "route_type", "route_count").Where("site_name = ?", site).Find(&siteRouteContent)

	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	var nestedRoutes []NestedRoute
	for _, route := range siteRouteContent {
		nestedRoute := NestedRoute{
			RouteType:  route.RouteType,
			RouteCount: route.RouteCount,
		}
		nestedRoutes = append(nestedRoutes, nestedRoute)
	}

	nestedSite := NestedSite{
		SiteName: site,
		Routes: nestedRoutes,
	}

	// Return the routes data for the specific site in the JSON response
	c.JSON(http.StatusOK, nestedSite)
}