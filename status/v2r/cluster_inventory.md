# V2R cluster inventory

2026-09-25T21:17:43.758486+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318704214016 available bytes; 82.22% used; 112476321 free inodes.

server1 `/home`: 318704214016 available bytes; 82.22% used; 112476321 free inodes.

server1 `/tmp`: 318704214016 available bytes; 82.22% used; 112476321 free inodes.

server1 `/var/tmp`: 318704214016 available bytes; 82.22% used; 112476321 free inodes.

server1 `/mnt/raid5`: 368332464128 available bytes; 98.31% used; 337539396 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22888423424 available bytes; 98.72% used; 110405692 free inodes.

server2 `/home`: 22888423424 available bytes; 98.72% used; 110405692 free inodes.

server2 `/tmp`: 22888423424 available bytes; 98.72% used; 110405692 free inodes.

server2 `/var/tmp`: 22888423424 available bytes; 98.72% used; 110405692 free inodes.

server2 `/mnt/raid5`: 301917110272 available bytes; 97.91% used; 445055653 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367511552 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84367511552 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 125900435456 available bytes; 98.26% used; 225807201 free inodes.

server3 `/tmp`: 84367511552 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84367511552 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389412352 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389412352 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217848279040 available bytes; 96.99% used; 224920387 free inodes.

server4 `/tmp`: 105389412352 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389412352 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
