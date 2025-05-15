# test_capabilities file
import pytest
from src.capabilities.hdf5_handler import HDF5Handler

@pytest.mark.asyncio
async def test_hdf5_handler_find_files():
    """Test HDF5 handler find_files operation."""
    handler = HDF5Handler()
    result = await handler.find_files({"directory": "/test/data", "pattern": "*.hdf5"})
    
    assert "files" in result
    assert isinstance(result["files"], list)
    assert len(result["files"]) > 0
    assert "count" in result
    assert result["count"] == len(result["files"])
    assert "directory" in result
    assert "pattern" in result
