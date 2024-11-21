def crowdfunding_trends_analysis(projects):
    """
    Analyze Crowdfunding Trends for Investing.
    
    :param projects: pd.DataFrame with project data (e.g., funding amount, backers).
    :return: List of top-performing projects.
    """
    projects['Funding Growth'] = projects['Funding Amount'].pct_change()
    top_projects = projects.sort_values(by='Funding Growth', ascending=False).head(5)
    
    print("Top Trending Crowdfunding Projects:")
    print(top_projects[['Project Name', 'Funding Growth']])
    
    return top_projects
