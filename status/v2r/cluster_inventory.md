# V2R cluster inventory

2026-09-26T07:32:38.300074+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318767853568 available bytes; 82.22% used; 112476289 free inodes.

server1 `/home`: 318767853568 available bytes; 82.22% used; 112476289 free inodes.

server1 `/tmp`: 318767853568 available bytes; 82.22% used; 112476289 free inodes.

server1 `/var/tmp`: 318767853568 available bytes; 82.22% used; 112476289 free inodes.

server1 `/mnt/raid5`: 219233652736 available bytes; 98.99% used; 337539238 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22318972928 available bytes; 98.75% used; 110403929 free inodes.

server2 `/home`: 22318972928 available bytes; 98.75% used; 110403929 free inodes.

server2 `/tmp`: 22318972928 available bytes; 98.75% used; 110403929 free inodes.

server2 `/var/tmp`: 22318972928 available bytes; 98.75% used; 110403929 free inodes.

server2 `/mnt/raid5`: 271381725184 available bytes; 98.12% used; 445026596 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82681606144 available bytes; 95.39% used; 114110901 free inodes.

server3 `/home`: 82681606144 available bytes; 95.39% used; 114110901 free inodes.

server3 `/data`: 123976720384 available bytes; 98.29% used; 225821045 free inodes.

server3 `/tmp`: 82681606144 available bytes; 95.39% used; 114110901 free inodes.

server3 `/var/tmp`: 82681606144 available bytes; 95.39% used; 114110901 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106074419200 available bytes; 94.08% used; 114348173 free inodes.

server4 `/home`: 106074419200 available bytes; 94.08% used; 114348173 free inodes.

server4 `/data`: 105867333632 available bytes; 98.54% used; 224922705 free inodes.

server4 `/tmp`: 106074419200 available bytes; 94.08% used; 114348173 free inodes.

server4 `/var/tmp`: 106074419200 available bytes; 94.08% used; 114348173 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
