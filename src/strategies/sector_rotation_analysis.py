def sector_rotation_analysis(sector_data, period='monthly'):
    """
    Sector Rotation Analysis.
    
    :param sector_data: pd.DataFrame with sector returns and dates.
    :param period: 'monthly' or 'quarterly'.
    :return: Top-performing sectors for each period.
    """
    df = sector_data.copy()
    df['Period'] = df['Date'].dt.to_period(period[0].upper())  # 'M' for monthly, 'Q' for quarterly
    period_performance = df.groupby('Period').mean()
    
    # Identify top-performing sectors
    top_sectors = period_performance.idxmax(axis=1)
    print("Top-Performing Sectors by Period:")
    print(top_sectors)
    
    return top_sectors
