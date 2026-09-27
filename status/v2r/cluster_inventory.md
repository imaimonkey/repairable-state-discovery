# V2R cluster inventory

2026-09-27T11:49:54.450243+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304694083584 available bytes; 83.00% used; 112401612 free inodes.

server1 `/home`: 304694083584 available bytes; 83.00% used; 112401612 free inodes.

server1 `/tmp`: 304694083584 available bytes; 83.00% used; 112401612 free inodes.

server1 `/var/tmp`: 304694083584 available bytes; 83.00% used; 112401612 free inodes.

server1 `/mnt/raid5`: 634689167360 available bytes; 97.09% used; 337424394 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16417615872 available bytes; 99.08% used; 110353088 free inodes.

server2 `/home`: 16417615872 available bytes; 99.08% used; 110353088 free inodes.

server2 `/tmp`: 16417615872 available bytes; 99.08% used; 110353088 free inodes.

server2 `/var/tmp`: 16417615872 available bytes; 99.08% used; 110353088 free inodes.

server2 `/mnt/raid5`: 569638522880 available bytes; 96.06% used; 444736551 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78543581184 available bytes; 95.62% used; 114062802 free inodes.

server3 `/home`: 78543581184 available bytes; 95.62% used; 114062802 free inodes.

server3 `/data`: 1331882356736 available bytes; 81.59% used; 225759183 free inodes.

server3 `/tmp`: 78543581184 available bytes; 95.62% used; 114062802 free inodes.

server3 `/var/tmp`: 78543581184 available bytes; 95.62% used; 114062802 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111029653504 available bytes; 93.80% used; 114372811 free inodes.

server4 `/home`: 111029653504 available bytes; 93.80% used; 114372811 free inodes.

server4 `/data`: 353040994304 available bytes; 95.12% used; 224728095 free inodes.

server4 `/tmp`: 111029653504 available bytes; 93.80% used; 114372811 free inodes.

server4 `/var/tmp`: 111029653504 available bytes; 93.80% used; 114372811 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
