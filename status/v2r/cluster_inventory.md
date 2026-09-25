# V2R cluster inventory

2026-09-25T14:01:51.406692+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319149535232 available bytes; 82.20% used; 112476966 free inodes.

server1 `/home`: 319149535232 available bytes; 82.20% used; 112476966 free inodes.

server1 `/tmp`: 319149535232 available bytes; 82.20% used; 112476966 free inodes.

server1 `/var/tmp`: 319149535232 available bytes; 82.20% used; 112476966 free inodes.

server1 `/mnt/raid5`: 364103507968 available bytes; 98.33% used; 337547486 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4734791680 available bytes; 99.74% used; 110407477 free inodes.

server2 `/home`: 4734791680 available bytes; 99.74% used; 110407477 free inodes.

server2 `/tmp`: 4734791680 available bytes; 99.74% used; 110407477 free inodes.

server2 `/var/tmp`: 4734791680 available bytes; 99.74% used; 110407477 free inodes.

server2 `/mnt/raid5`: 322237755392 available bytes; 97.77% used; 445076237 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 84281503744 available bytes; 95.30% used; 114154477 free inodes.

server3 `/home`: 84281503744 available bytes; 95.30% used; 114154477 free inodes.

server3 `/data`: 142222651392 available bytes; 98.03% used; 225809163 free inodes.

server3 `/tmp`: 84281503744 available bytes; 95.30% used; 114154477 free inodes.

server3 `/var/tmp`: 84281503744 available bytes; 95.30% used; 114154477 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655107584 available bytes; 94.10% used; 114349712 free inodes.

server4 `/home`: 105655107584 available bytes; 94.10% used; 114349712 free inodes.

server4 `/data`: 231493726208 available bytes; 96.80% used; 224948336 free inodes.

server4 `/tmp`: 105655107584 available bytes; 94.10% used; 114349712 free inodes.

server4 `/var/tmp`: 105655107584 available bytes; 94.10% used; 114349712 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
