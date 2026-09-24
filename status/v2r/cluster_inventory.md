# V2R cluster inventory

2026-09-24T00:04:10.616841+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325578575872 available bytes; 81.84% used; 112500869 free inodes.

server1 `/home`: 325578575872 available bytes; 81.84% used; 112500869 free inodes.

server1 `/tmp`: 325578575872 available bytes; 81.84% used; 112500869 free inodes.

server1 `/var/tmp`: 325578575872 available bytes; 81.84% used; 112500869 free inodes.

server1 `/mnt/raid5`: 1250524823552 available bytes; 94.26% used; 337735470 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41016827904 available bytes; 97.71% used; 110432431 free inodes.

server2 `/home`: 41016827904 available bytes; 97.71% used; 110432431 free inodes.

server2 `/tmp`: 41016827904 available bytes; 97.71% used; 110432431 free inodes.

server2 `/var/tmp`: 41016827904 available bytes; 97.71% used; 110432431 free inodes.

server2 `/mnt/raid5`: 533478465536 available bytes; 96.31% used; 445204015 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292797915136 available bytes; 83.66% used; 114213304 free inodes.

server3 `/home`: 292797915136 available bytes; 83.66% used; 114213304 free inodes.

server3 `/data`: 82265710592 available bytes; 98.86% used; 225844776 free inodes.

server3 `/tmp`: 292797915136 available bytes; 83.66% used; 114213304 free inodes.

server3 `/var/tmp`: 292797915136 available bytes; 83.66% used; 114213304 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106129960960 available bytes; 94.08% used; 114351131 free inodes.

server4 `/home`: 106129960960 available bytes; 94.08% used; 114351131 free inodes.

server4 `/data`: 292917477376 available bytes; 95.95% used; 225414607 free inodes.

server4 `/tmp`: 106129960960 available bytes; 94.08% used; 114351131 free inodes.

server4 `/var/tmp`: 106129960960 available bytes; 94.08% used; 114351131 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
