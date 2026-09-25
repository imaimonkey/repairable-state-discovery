# V2R cluster inventory

2026-09-25T13:47:53.866819+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319160238080 available bytes; 82.20% used; 112476970 free inodes.

server1 `/home`: 319160238080 available bytes; 82.20% used; 112476970 free inodes.

server1 `/tmp`: 319160238080 available bytes; 82.20% used; 112476970 free inodes.

server1 `/var/tmp`: 319160238080 available bytes; 82.20% used; 112476970 free inodes.

server1 `/mnt/raid5`: 364125970432 available bytes; 98.33% used; 337547585 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 18781085696 available bytes; 98.95% used; 110408217 free inodes.

server2 `/home`: 18781085696 available bytes; 98.95% used; 110408217 free inodes.

server2 `/tmp`: 18781085696 available bytes; 98.95% used; 110408217 free inodes.

server2 `/var/tmp`: 18781085696 available bytes; 98.95% used; 110408217 free inodes.

server2 `/mnt/raid5`: 322135093248 available bytes; 97.77% used; 445076647 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84281057280 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84281057280 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142343675904 available bytes; 98.03% used; 225809417 free inodes.

server3 `/tmp`: 84281057280 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84281057280 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655480320 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655480320 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231461244928 available bytes; 96.80% used; 224949898 free inodes.

server4 `/tmp`: 105655480320 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655480320 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
