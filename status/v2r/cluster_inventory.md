# V2R cluster inventory

2026-09-27T11:15:03.371164+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304693702656 available bytes; 83.00% used; 112401721 free inodes.

server1 `/home`: 304693702656 available bytes; 83.00% used; 112401721 free inodes.

server1 `/tmp`: 304693702656 available bytes; 83.00% used; 112401721 free inodes.

server1 `/var/tmp`: 304693702656 available bytes; 83.00% used; 112401721 free inodes.

server1 `/mnt/raid5`: 635398553600 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16442576896 available bytes; 99.08% used; 110353720 free inodes.

server2 `/home`: 16442576896 available bytes; 99.08% used; 110353720 free inodes.

server2 `/tmp`: 16442576896 available bytes; 99.08% used; 110353720 free inodes.

server2 `/var/tmp`: 16442576896 available bytes; 99.08% used; 110353720 free inodes.

server2 `/mnt/raid5`: 570626650112 available bytes; 96.06% used; 444737369 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543773696 available bytes; 95.62% used; 114062815 free inodes.

server3 `/home`: 78543773696 available bytes; 95.62% used; 114062815 free inodes.

server3 `/data`: 1332000460800 available bytes; 81.59% used; 225759795 free inodes.

server3 `/tmp`: 78543773696 available bytes; 95.62% used; 114062815 free inodes.

server3 `/var/tmp`: 78543773696 available bytes; 95.62% used; 114062815 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111030644736 available bytes; 93.80% used; 114372822 free inodes.

server4 `/home`: 111030644736 available bytes; 93.80% used; 114372822 free inodes.

server4 `/data`: 353786298368 available bytes; 95.11% used; 224728306 free inodes.

server4 `/tmp`: 111030644736 available bytes; 93.80% used; 114372822 free inodes.

server4 `/var/tmp`: 111030644736 available bytes; 93.80% used; 114372822 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
