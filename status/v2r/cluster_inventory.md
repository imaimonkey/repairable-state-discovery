# V2R cluster inventory

2026-09-26T07:29:35.017582+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318768455680 available bytes; 82.22% used; 112476291 free inodes.

server1 `/home`: 318768455680 available bytes; 82.22% used; 112476291 free inodes.

server1 `/tmp`: 318768455680 available bytes; 82.22% used; 112476291 free inodes.

server1 `/var/tmp`: 318768455680 available bytes; 82.22% used; 112476291 free inodes.

server1 `/mnt/raid5`: 219239182336 available bytes; 98.99% used; 337539243 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22321946624 available bytes; 98.75% used; 110403925 free inodes.

server2 `/home`: 22321946624 available bytes; 98.75% used; 110403925 free inodes.

server2 `/tmp`: 22321946624 available bytes; 98.75% used; 110403925 free inodes.

server2 `/var/tmp`: 22321946624 available bytes; 98.75% used; 110403925 free inodes.

server2 `/mnt/raid5`: 271510523904 available bytes; 98.12% used; 445027003 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82679848960 available bytes; 95.39% used; 114110897 free inodes.

server3 `/home`: 82679848960 available bytes; 95.39% used; 114110897 free inodes.

server3 `/data`: 123977662464 available bytes; 98.29% used; 225821097 free inodes.

server3 `/tmp`: 82679848960 available bytes; 95.39% used; 114110897 free inodes.

server3 `/var/tmp`: 82679848960 available bytes; 95.39% used; 114110897 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106074521600 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106074521600 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105859735552 available bytes; 98.54% used; 224922720 free inodes.

server4 `/tmp`: 106074521600 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106074521600 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
