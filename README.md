->Holiday Data & Temporal Feature Engineering

The holiday dataset was processed to move beyond simple date markers into a format capable of capturing human behavioral patterns. The day_of_week feature was explicitly preserved alongside the is_bank_holiday indicator.

The rationale is grounded in Social Rhythm Theory: incident rates for both fires and accidents do not occur in isolation but are tied to weekly cycles. For example, a Bank Holiday on a Friday creates a different risk profile (travel surges, prolonged social activity) compared to a midweek holiday. By retaining the day of the week, the model can distinguish between standard "Weekend Effects" and unique "Holiday Effects," capturing the complex temporal interactions required for accurate risk prediction.


->Data Alignment and Statistical Validation

To ensure the integrity of the integrated dataset (Weather, Energy, Accidents, and Holidays), a standardized synchronization pipeline was implemented:

Temporal Synchronization: All records were filtered to the 2010–2020 timeframe to ensure cross-dataset consistency.

Audit Verification: A pre-cleaning check was executed, resulting in a "Check Complete - Data is Valid for Cleaning" status, confirming that the remaining features provide a clean signal for PCA (Principal Component Analysis).

Standardization: Feature names were normalized to lowercase and categorical labels (Is_Bank_Holiday) were converted to boolean integers, facilitating an error-free merge across heterogeneous sources. 
