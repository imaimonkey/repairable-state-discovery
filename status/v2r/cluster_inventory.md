# V2R cluster inventory

2026-09-26T01:50:37.082226+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318528237568 available bytes; 82.23% used; 112476288 free inodes.

server1 `/home`: 318528237568 available bytes; 82.23% used; 112476288 free inodes.

server1 `/tmp`: 318528237568 available bytes; 82.23% used; 112476288 free inodes.

server1 `/var/tmp`: 318528237568 available bytes; 82.23% used; 112476288 free inodes.

server1 `/mnt/raid5`: 345247670272 available bytes; 98.42% used; 337546347 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22937837568 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22937837568 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22937837568 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22937837568 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 290125193216 available bytes; 98.00% used; 445055393 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84326879232 available bytes; 95.29% used; 114152366 free inodes.

server3 `/home`: 84326879232 available bytes; 95.29% used; 114152366 free inodes.

server3 `/data`: 124793569280 available bytes; 98.28% used; 225817677 free inodes.

server3 `/tmp`: 84326879232 available bytes; 95.29% used; 114152366 free inodes.

server3 `/var/tmp`: 84326879232 available bytes; 95.29% used; 114152366 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105434021888 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105434021888 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130903478272 available bytes; 98.19% used; 224915771 free inodes.

server4 `/tmp`: 105434021888 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105434021888 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
