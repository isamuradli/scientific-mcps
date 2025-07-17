#!/usr/bin/env python3
"""
Demo script showing PDF download capabilities.
"""
import asyncio
import tempfile
import os
from src.arxiv_mcp.capabilities.pdf_download import (
    download_paper_pdf,
    get_pdf_url,
    download_multiple_pdfs
)


async def main():
    """Demo the PDF download capabilities."""
    print("ArXiv MCP PDF Download Demo")
    print("=" * 40)
    
    # Example ArXiv ID - "Attention Is All You Need"
    arxiv_id = "1706.03762"
    
    try:
        # Demo 1: Get PDF URL
        print(f"\n1. Getting PDF URL for paper {arxiv_id}...")
        url_result = await get_pdf_url(arxiv_id)
        if url_result['success']:
            print(f"   ✓ PDF URL: {url_result['pdf_url']}")
            print(f"   ✓ Content Type: {url_result['content_type']}")
            print(f"   ✓ Content Length: {url_result['content_length']} bytes")
        else:
            print(f"   ✗ Failed to get PDF URL")
        
        # Demo 2: Download single PDF
        print(f"\n2. Downloading PDF for paper {arxiv_id}...")
        with tempfile.TemporaryDirectory() as temp_dir:
            download_result = await download_paper_pdf(arxiv_id, temp_dir)
            if download_result['success']:
                print(f"   ✓ Downloaded to: {download_result['file_path']}")
                print(f"   ✓ File size: {download_result['file_size']} bytes")
                print(f"   ✓ Filename: {download_result['filename']}")
            else:
                print(f"   ✗ Failed to download PDF")
        
        # Demo 3: Download multiple PDFs
        print(f"\n3. Downloading multiple PDFs...")
        arxiv_ids = ["1706.03762", "2301.12345"]  # Second might not exist
        with tempfile.TemporaryDirectory() as temp_dir:
            batch_result = await download_multiple_pdfs(arxiv_ids, temp_dir, max_concurrent=2)
            if batch_result['success']:
                print(f"   ✓ Total requested: {batch_result['total_requested']}")
                print(f"   ✓ Successful downloads: {batch_result['successful_downloads']}")
                print(f"   ✓ Failed downloads: {batch_result['failed_downloads']}")
                print(f"   ✓ Download path: {batch_result['download_path']}")
                
                # Show results for each paper
                for result in batch_result['results']:
                    if result.get('success'):
                        print(f"     ✓ {result['arxiv_id']}: {result['filename']}")
                    else:
                        print(f"     ✗ {result['arxiv_id']}: {result.get('error', 'Unknown error')}")
            else:
                print(f"   ✗ Batch download failed")
        
    except Exception as e:
        print(f"Demo failed: {e}")
    
    print("\nDemo completed!")


if __name__ == "__main__":
    asyncio.run(main())