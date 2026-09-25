# V2R cluster inventory

2026-09-25T22:38:21.452332+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318693834752 available bytes; 82.22% used; 112476307 free inodes.

server1 `/home`: 318693834752 available bytes; 82.22% used; 112476307 free inodes.

server1 `/tmp`: 318693834752 available bytes; 82.22% used; 112476307 free inodes.

server1 `/var/tmp`: 318693834752 available bytes; 82.22% used; 112476307 free inodes.

server1 `/mnt/raid5`: 360225783808 available bytes; 98.35% used; 337538900 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22951976960 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22951976960 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22951976960 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22951976960 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 298729762816 available bytes; 97.94% used; 445052815 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351164416 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84351164416 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124824461312 available bytes; 98.27% used; 225805804 free inodes.

server3 `/tmp`: 84351164416 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84351164416 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105235804160 available bytes; 94.13% used; 114346964 free inodes.

server4 `/home`: 105235804160 available bytes; 94.13% used; 114346964 free inodes.

server4 `/data`: 192232169472 available bytes; 97.34% used; 224917690 free inodes.

server4 `/tmp`: 105235804160 available bytes; 94.13% used; 114346964 free inodes.

server4 `/var/tmp`: 105235804160 available bytes; 94.13% used; 114346964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
