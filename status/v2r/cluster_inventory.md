# V2R cluster inventory

2026-09-27T09:07:03.126042+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314465402880 available bytes; 82.46% used; 112440732 free inodes.

server1 `/home`: 314465402880 available bytes; 82.46% used; 112440732 free inodes.

server1 `/tmp`: 314465402880 available bytes; 82.46% used; 112440732 free inodes.

server1 `/var/tmp`: 314465402880 available bytes; 82.46% used; 112440732 free inodes.

server1 `/mnt/raid5`: 634582114304 available bytes; 97.09% used; 337400191 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16508624896 available bytes; 99.08% used; 110356972 free inodes.

server2 `/home`: 16508624896 available bytes; 99.08% used; 110356972 free inodes.

server2 `/tmp`: 16508624896 available bytes; 99.08% used; 110356972 free inodes.

server2 `/var/tmp`: 16508624896 available bytes; 99.08% used; 110356972 free inodes.

server2 `/mnt/raid5`: 574359474176 available bytes; 96.03% used; 444743555 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78556487680 available bytes; 95.62% used; 114062917 free inodes.

server3 `/home`: 78556487680 available bytes; 95.62% used; 114062917 free inodes.

server3 `/data`: 1332577042432 available bytes; 81.58% used; 225762877 free inodes.

server3 `/tmp`: 78556487680 available bytes; 95.62% used; 114062917 free inodes.

server3 `/var/tmp`: 78556487680 available bytes; 95.62% used; 114062917 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051087872 available bytes; 93.80% used; 114372859 free inodes.

server4 `/home`: 111051087872 available bytes; 93.80% used; 114372859 free inodes.

server4 `/data`: 364325875712 available bytes; 94.96% used; 224768173 free inodes.

server4 `/tmp`: 111051087872 available bytes; 93.80% used; 114372859 free inodes.

server4 `/var/tmp`: 111051087872 available bytes; 93.80% used; 114372859 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
