# V2R cluster inventory

2026-09-25T17:31:27.029435+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318680424448 available bytes; 82.22% used; 112476352 free inodes.

server1 `/home`: 318680424448 available bytes; 82.22% used; 112476352 free inodes.

server1 `/tmp`: 318680424448 available bytes; 82.22% used; 112476352 free inodes.

server1 `/var/tmp`: 318680424448 available bytes; 82.22% used; 112476352 free inodes.

server1 `/mnt/raid5`: 363833991168 available bytes; 98.33% used; 337543076 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23105187840 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23105187840 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23105187840 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23105187840 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 315442761728 available bytes; 97.82% used; 445067947 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84393902080 available bytes; 95.29% used; 114152610 free inodes.

server3 `/home`: 84393902080 available bytes; 95.29% used; 114152610 free inodes.

server3 `/data`: 132778975232 available bytes; 98.16% used; 225811202 free inodes.

server3 `/tmp`: 84393902080 available bytes; 95.29% used; 114152610 free inodes.

server3 `/var/tmp`: 84393902080 available bytes; 95.29% used; 114152610 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105617625088 available bytes; 94.11% used; 114349642 free inodes.

server4 `/home`: 105617625088 available bytes; 94.11% used; 114349642 free inodes.

server4 `/data`: 229867585536 available bytes; 96.82% used; 224932840 free inodes.

server4 `/tmp`: 105617625088 available bytes; 94.11% used; 114349642 free inodes.

server4 `/var/tmp`: 105617625088 available bytes; 94.11% used; 114349642 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
