# V2R cluster inventory

2026-09-24T02:36:52.630230+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325385490432 available bytes; 81.85% used; 112498808 free inodes.

server1 `/home`: 325385490432 available bytes; 81.85% used; 112498808 free inodes.

server1 `/tmp`: 325385490432 available bytes; 81.85% used; 112498808 free inodes.

server1 `/var/tmp`: 325385490432 available bytes; 81.85% used; 112498808 free inodes.

server1 `/mnt/raid5`: 618505969664 available bytes; 97.16% used; 337733209 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40887758848 available bytes; 97.72% used; 110431490 free inodes.

server2 `/home`: 40887758848 available bytes; 97.72% used; 110431490 free inodes.

server2 `/tmp`: 40887758848 available bytes; 97.72% used; 110431490 free inodes.

server2 `/var/tmp`: 40887758848 available bytes; 97.72% used; 110431490 free inodes.

server2 `/mnt/raid5`: 528799191040 available bytes; 96.35% used; 445199244 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292289253376 available bytes; 83.69% used; 114187090 free inodes.

server3 `/home`: 292289253376 available bytes; 83.69% used; 114187090 free inodes.

server3 `/data`: 39746523136 available bytes; 99.45% used; 225846194 free inodes.

server3 `/tmp`: 292289253376 available bytes; 83.69% used; 114187090 free inodes.

server3 `/var/tmp`: 292289253376 available bytes; 83.69% used; 114187090 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003353600 available bytes; 94.08% used; 114349834 free inodes.

server4 `/home`: 106003353600 available bytes; 94.08% used; 114349834 free inodes.

server4 `/data`: 289731497984 available bytes; 96.00% used; 225387392 free inodes.

server4 `/tmp`: 106003353600 available bytes; 94.08% used; 114349834 free inodes.

server4 `/var/tmp`: 106003353600 available bytes; 94.08% used; 114349834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
