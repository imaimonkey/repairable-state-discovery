# V2R cluster inventory

2026-09-25T17:49:47.577132+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318670118912 available bytes; 82.22% used; 112476354 free inodes.

server1 `/home`: 318670118912 available bytes; 82.22% used; 112476354 free inodes.

server1 `/tmp`: 318670118912 available bytes; 82.22% used; 112476354 free inodes.

server1 `/var/tmp`: 318670118912 available bytes; 82.22% used; 112476354 free inodes.

server1 `/mnt/raid5`: 371241635840 available bytes; 98.30% used; 337542733 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23095369728 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23095369728 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23095369728 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23095369728 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 315481038848 available bytes; 97.82% used; 445068474 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84390535168 available bytes; 95.29% used; 114152617 free inodes.

server3 `/home`: 84390535168 available bytes; 95.29% used; 114152617 free inodes.

server3 `/data`: 132537020416 available bytes; 98.17% used; 225810768 free inodes.

server3 `/tmp`: 84390535168 available bytes; 95.29% used; 114152617 free inodes.

server3 `/var/tmp`: 84390535168 available bytes; 95.29% used; 114152617 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105617014784 available bytes; 94.11% used; 114349621 free inodes.

server4 `/home`: 105617014784 available bytes; 94.11% used; 114349621 free inodes.

server4 `/data`: 229799624704 available bytes; 96.82% used; 224932594 free inodes.

server4 `/tmp`: 105617014784 available bytes; 94.11% used; 114349621 free inodes.

server4 `/var/tmp`: 105617014784 available bytes; 94.11% used; 114349621 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
