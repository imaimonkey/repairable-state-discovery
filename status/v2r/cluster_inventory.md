# V2R cluster inventory

2026-09-25T13:37:10.125285+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319182381056 available bytes; 82.19% used; 112477030 free inodes.

server1 `/home`: 319182381056 available bytes; 82.19% used; 112477030 free inodes.

server1 `/tmp`: 319182381056 available bytes; 82.19% used; 112477030 free inodes.

server1 `/var/tmp`: 319182381056 available bytes; 82.19% used; 112477030 free inodes.

server1 `/mnt/raid5`: 364193021952 available bytes; 98.33% used; 337547735 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 16538759168 available bytes; 99.08% used; 110408646 free inodes.

server2 `/home`: 16538759168 available bytes; 99.08% used; 110408646 free inodes.

server2 `/tmp`: 16538759168 available bytes; 99.08% used; 110408646 free inodes.

server2 `/var/tmp`: 16538759168 available bytes; 99.08% used; 110408646 free inodes.

server2 `/mnt/raid5`: 323258146816 available bytes; 97.77% used; 445077243 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84281085952 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84281085952 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142350589952 available bytes; 98.03% used; 225809583 free inodes.

server3 `/tmp`: 84281085952 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84281085952 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655803904 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655803904 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231394058240 available bytes; 96.80% used; 224951185 free inodes.

server4 `/tmp`: 105655803904 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655803904 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
