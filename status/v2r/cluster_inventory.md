# V2R cluster inventory

2026-09-27T03:03:49.922378+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315086721024 available bytes; 82.42% used; 112443033 free inodes.

server1 `/home`: 315086721024 available bytes; 82.42% used; 112443033 free inodes.

server1 `/tmp`: 315086721024 available bytes; 82.42% used; 112443033 free inodes.

server1 `/var/tmp`: 315086721024 available bytes; 82.42% used; 112443033 free inodes.

server1 `/mnt/raid5`: 636810981376 available bytes; 97.08% used; 337401386 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17633935360 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17633935360 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17633935360 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17633935360 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 579447173120 available bytes; 96.00% used; 444883640 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78706753536 available bytes; 95.61% used; 114062938 free inodes.

server3 `/home`: 78706753536 available bytes; 95.61% used; 114062938 free inodes.

server3 `/data`: 1336552079360 available bytes; 81.53% used; 225761796 free inodes.

server3 `/tmp`: 78706753536 available bytes; 95.61% used; 114062938 free inodes.

server3 `/var/tmp`: 78706753536 available bytes; 95.61% used; 114062938 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111030910976 available bytes; 93.80% used; 114373046 free inodes.

server4 `/home`: 111030910976 available bytes; 93.80% used; 114373046 free inodes.

server4 `/data`: 396841963520 available bytes; 94.52% used; 224781056 free inodes.

server4 `/tmp`: 111030910976 available bytes; 93.80% used; 114373046 free inodes.

server4 `/var/tmp`: 111030910976 available bytes; 93.80% used; 114373046 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
