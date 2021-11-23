use pyo3::prelude::*;

#[pyfunction]
fn multiply(a: isize, b: isize) -> PyResult<isize> {
    Ok(a * b)
}

#[pyfunction]
fn list_sum(a: Vec<isize>) -> PyResult<isize> {
    let mut sum: isize = 0;
    for i in a {
        sum += i;
    }
    Ok(sum)
}

#[pymodule]
#[pyo3(name = "timing_example")]
fn timing_example(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(multiply, m)?)?;
    m.add_function(wrap_pyfunction!(list_sum, m)?)?;
    Ok(())
}
