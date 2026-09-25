# V2R cluster inventory

2026-09-25T18:38:43.517291+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318749384704 available bytes; 82.22% used; 112476345 free inodes.

server1 `/home`: 318749384704 available bytes; 82.22% used; 112476345 free inodes.

server1 `/tmp`: 318749384704 available bytes; 82.22% used; 112476345 free inodes.

server1 `/var/tmp`: 318749384704 available bytes; 82.22% used; 112476345 free inodes.

server1 `/mnt/raid5`: 371172093952 available bytes; 98.30% used; 337541584 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23102939136 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23102939136 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23102939136 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23102939136 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 313177509888 available bytes; 97.84% used; 445066283 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382134272 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84382134272 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131388375040 available bytes; 98.18% used; 225809599 free inodes.

server3 `/tmp`: 84382134272 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84382134272 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105607278592 available bytes; 94.11% used; 114349600 free inodes.

server4 `/home`: 105607278592 available bytes; 94.11% used; 114349600 free inodes.

server4 `/data`: 229696655360 available bytes; 96.83% used; 224931642 free inodes.

server4 `/tmp`: 105607278592 available bytes; 94.11% used; 114349600 free inodes.

server4 `/var/tmp`: 105607278592 available bytes; 94.11% used; 114349600 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
