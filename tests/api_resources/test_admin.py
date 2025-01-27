# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from zeroentropy import ZeroEntropy, AsyncZeroEntropy
from zeroentropy.types import AdminCreateOrganizationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_organization(self, client: ZeroEntropy) -> None:
        admin = client.admin.create_organization(
            organization_name="organization_name",
        )
        assert_matches_type(AdminCreateOrganizationResponse, admin, path=["response"])

    @parametrize
    def test_raw_response_create_organization(self, client: ZeroEntropy) -> None:
        response = client.admin.with_raw_response.create_organization(
            organization_name="organization_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminCreateOrganizationResponse, admin, path=["response"])

    @parametrize
    def test_streaming_response_create_organization(self, client: ZeroEntropy) -> None:
        with client.admin.with_streaming_response.create_organization(
            organization_name="organization_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminCreateOrganizationResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_organization(self, async_client: AsyncZeroEntropy) -> None:
        admin = await async_client.admin.create_organization(
            organization_name="organization_name",
        )
        assert_matches_type(AdminCreateOrganizationResponse, admin, path=["response"])

    @parametrize
    async def test_raw_response_create_organization(self, async_client: AsyncZeroEntropy) -> None:
        response = await async_client.admin.with_raw_response.create_organization(
            organization_name="organization_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminCreateOrganizationResponse, admin, path=["response"])

    @parametrize
    async def test_streaming_response_create_organization(self, async_client: AsyncZeroEntropy) -> None:
        async with async_client.admin.with_streaming_response.create_organization(
            organization_name="organization_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminCreateOrganizationResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
